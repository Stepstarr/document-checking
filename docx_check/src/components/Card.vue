<template>
  <div class="card mb-3">
    <header class="card-header">
      <p class="card-header-title">{{cardName}}</p>
      <button class="card-header-icon" aria-label="more options" @click="isClosed = !isClosed">
        <span class="icon">
          <i class="fas" :class="isClosed ? 'fa-angle-down' : 'fa-angle-up'" aria-hidden="true"></i>
        </span>
      </button>
    </header>
    <div class="card-content" v-show="!isClosed">
      <div v-for="(model, i) in sectionModels" :key="'page-layout-section-'+i">
        <CardText v-if="model.component == 'CardText'" :name="model.name" :value="model.data" :isEditable="isEditable" @value-changed="onValueChanged"></CardText>
        <Section v-if="model.component == 'Section'" :name="model.name" :modelData="model.data" :modelTypes="model.types" :isEditable="isEditable" @value-changed="onValueChanged"></Section>
      </div>
    </div>
  </div>
</template>
    
<script>
import CardText from './CardText.vue'
import Section from './Section.vue'


export default {
  name: 'Card',
  components: {
    CardText,
    Section
  },
  props: ['cardData', 'cardName', 'cardSections', 'isEditable'],
  data () {
    return {
      isClosed: false,
      sectionModels: [],
    }
  },
  watch: {
    cardData (val) {
      if (val) {
        this.sectionModels = this.makeSectionModels(val)
      }
    },
  },
  methods: {
    makeSectionModels (value) {
      var models = []
      for (var section of this.cardSections) {
        if (section.name in value) {
          var model = {
            name: section.name,
            component: section.component,
            data: value[section.name],
            types: section.modelTypes,
          }
          models.push(model)
        }
      }
      return models
    },
    onValueChanged (val) {
      if (!this.cardData || !this.isEditable) {
        return
      }
      var name = val[0]
      var value = val[1]
      var cardData = JSON.parse(JSON.stringify(this.cardData))
      cardData[name] = value
      this.$emit('value-changed', [this.cardName, cardData])
    },
  },
  mounted () {
    this.sectionModels = this.makeSectionModels(this.cardData)
  }
}
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
  