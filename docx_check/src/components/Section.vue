<template>
  <div class="columns mt-3">
    <div class="column is-3 has-text-left">
      <label class="label section-label">{{name}}</label>
    </div>
    <div class="column">
      <div v-for="(f, i) in fields" :key="'model-field-' + name + '-' + i">
        <SectionNumber v-if="f.component == 'SectionNumber'" :name="f.name" :value="f.value" :unit="f.unit" :isEditable="isEditable" @value-changed="onValueChanged"></SectionNumber>
        <SectionSelect v-if="f.component == 'SectionSelect'" :name="f.name" :value="f.value" :options="f.options" :isEditable="isEditable" @value-changed="onValueChanged"></SectionSelect>
      </div>
    </div>
  </div>
</template>

<script>
import SectionNumber from './SectionNumber.vue'
import SectionSelect from './SectionSelect.vue'

export default {
  name: 'Section',
  components: {
    SectionNumber,
    SectionSelect
  },
  props: ['name', 'modelData', 'modelTypes', 'isEditable'],
  data () {
    return {
      fields: []
    }
  },
  methods: {
    makeFields (data) {
      var fields = []
      for (const modelType of this.modelTypes) {
        if (modelType.name in data) {
          var field = {
            name: modelType.name,
            component: modelType.component,
            unit: modelType.unit,
            value: data[modelType.name],
            options: modelType.options
          }
          fields.push(field)
        }
      }
      return fields
    },
    onValueChanged (val) {
      if (!this.modelData || !this.isEditable) {
        return
      }
      var name = val[0]
      var value = val[1]
      var modelData = JSON.parse(JSON.stringify(this.modelData))
      modelData[name] = value
      this.$emit('value-changed', [this.name, modelData])
    },
  },
  mounted () {
    this.fields = this.makeFields(this.modelData)
  }
}
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.section-label {
  padding-top: 5px;
}
</style>
  