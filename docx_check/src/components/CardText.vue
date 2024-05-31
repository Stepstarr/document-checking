<template>
  <div class="columns is-variable is-vcentered">
    <div class="column is-3 has-text-left">
      <label class="label">{{name}}</label>
    </div>
    <div class="column">
      <input class="input" type="text" v-model="localValue" :readonly="!isEditable"/>
    </div>
  </div>
</template>
    
<script>
export default {
  name: 'CardText',
  props: ['name', 'value', 'isEditable'],
  data () {
    return {
      localValue: ''
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
      var localValue = null
      var value = ''
      if (this.value) {
        value = String(this.value)
      }
      localValue = value
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

</style>
