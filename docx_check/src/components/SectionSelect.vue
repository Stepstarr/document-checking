<template>
  <div class="columns is-variable is-vcentered">
    <div class="column is-one-third has-text-right">
      <p>{{name}}</p>
    </div>
    <div class="column is-6 ">
      <div class="select is-fullwidth">
        <select v-model="localValue" :disabled="!isEditable" :class="{'disabled-select': !isEditable}">
          <option v-for="(option, i) in options" :key="name + '-option-' + i" :value="option.value">{{option.label}}</option>
        </select>
      </div>
    </div>
  </div>
</template>
    
<script>
export default {
  name: 'SectionSelect',
  props: ['name', 'value', 'options', 'isEditable'],
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
      if (this.value != this.localValue) {
        this.localValue = this.value
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
.disabled-select {
  color: #111111!important;
}
</style>
