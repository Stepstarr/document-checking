<template>
  <div class="box">
    <div class="columns is-variable is-vcentered">
        <div class="column is-3 ">
            <label class="label">当前模板:</label>
        </div>
        <div class="column has-text-left">
            <p>{{ templateName }}</p>
        </div>
    </div>
  </div>
    
  <div>
    <div v-for="(card, i) in cardModels" :key="'card-' + i">
      <Card :cardData="card.data" :cardName="card.name" :cardSections="card.sections" :isEditable="isEditable" @value-changed="onValueChanged" />
    </div>
  </div>
</template>
  
<script>
import Card from './Card.vue'
import { modelConfig } from '../utils/modelTypes.js'


export default {
  name: 'DocTemplate',
  components: {
    Card
  },
  props: ['templateName', 'templateData', 'isEditable'],
  data () {
    return {
      cards: modelConfig,
      cardModels: [],
    }
  },
  watch: {
    templateData (val) {
      if (val) {
        this.cardModels = this.makeCardModels(val)
      }
    },
  },
  methods: {
    makeCardModels (value) {
      var cardModels = []
      for (var card of this.cards) {
        if (card.name in value) {
          var cardModel = {
            name: card.name,
            data: value[card.name],
            sections: card.sections,
          }
          cardModels.push(cardModel)
        }
      }
      return cardModels
    },
    onValueChanged (val) {
      if (!this.templateData || !this.isEditable) {
        return
      }
      var name = val[0]
      var value = val[1]
      var templateData = JSON.parse(JSON.stringify(this.templateData))
      templateData[name] = value
      this.$emit('update-template-value', templateData)
    },
  },
  mounted () {
    if (this.templateData) {
      this.cardModels = this.makeCardModels(this.templateData)
    }
  },
}
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
