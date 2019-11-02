<template>
  <tr>
    <td>{{ day }} {{timeOption}}</td>
  </tr>
</template>

<script>
export default {
  name: 'EventOption',
  props:['day','timeOption']
}
</script>