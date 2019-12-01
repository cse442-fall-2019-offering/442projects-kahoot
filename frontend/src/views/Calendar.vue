<template>
  <div class="pl-5 pr-5" style="padding-top: 80px;">
    <iframe 
      :src="`https://calendar.google.com/calendar/embed?src=${$route.params.id}&ctz=America%2FNew_York`"
      style="border: 0" 
      width="100%" 
      height="700" 
      frameborder="0" 
      scrolling="no"
    >
    </iframe>
  </div>
</template>

<script>

export default {
}
</script>

<style lang="scss">
.content {
  margin-left: 160px;
  padding-top: 55px;
}
</style>