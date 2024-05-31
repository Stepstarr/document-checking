<template>
  <my-header/>
  <div class="container">
    <div class="columns is-variable">
      <div class="column is-7 has-text-left">
        <my-fChecker :templateName="tName"/>
      </div>
      <div class="column has-text-left">
        <my-fTemplate :applyTemplate="tName" @update-value="updateValue($event)"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      tName: null,
    }
  },
  methods: {
    updateValue(newValue) {
      this.tName = newValue;
    }
  }
}
</script>