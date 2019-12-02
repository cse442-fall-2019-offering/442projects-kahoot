<template>
  <tr>
    <td>{{weeks}} {{practices}} {{sdate}}</td>
   
  </tr>
</template>

<script>
export default {
  name: 'ScheduleOptions',
  props: ['weeks','practices','sdate']
}
</script>