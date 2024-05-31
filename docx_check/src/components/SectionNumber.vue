<template>
  <div class="columns is-variable is-vcentered">
    <div class="column is-4 is-one-third has-text-right">
      <p>{{name}}</p>
    </div>
    <div class="column is-5 is-centered">
      <input class="input" type="number" v-model.number="localValue" :readonly="!isEditable">
    </div>
    <div class="column is-3 has-text-left my-unit">
      <p>{{unit}}</p>
    </div>
  </div>
</template>
    
<script>
export default {
  name: 'SectionNumber',
  props: ['name', 'value', 'unit', 'isEditable'],
  data () {
    return {
      localValue: null
    }
  },
  watch: {
    value: function (val) {
      this.setLocalValue()
    },
    localValue: function (val) {
      this.$nextTick(function () {
        if (this.isEditable) {
          this.$emit('value-changed', [this.name, val])
        }
      })
    },
  },
  methods: {
    setLocalValue () {
      var value = 0
      if (this.value) {
        value = this.value
      }
      var localValue = value
      if (localValue != this.localValue) {
        this.localValue = localValue
      }
    },
  },
  mounted () {
    this.setLocalValue()
  }
}
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.my-unit {
  padding-left: 0px!important;
}
</style>