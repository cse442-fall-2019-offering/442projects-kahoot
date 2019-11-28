<template>
  <tr>
    <td   class="align-center col-2">{{ day }} {{timeOption}}</td>
  </tr>
</template>

<script>
export default {
  name: 'EventOption',
  props:['day','timeOption']
}
</script>
