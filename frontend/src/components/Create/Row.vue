<template>
  <tr>
    <td>{{ team }} {{weeks}} {{practices}} {{games}} {{sdate}}</td>
   
  </tr>
</template>

<script>
export default {
  name: 'Row',
  props: ['team','weeks','practices','games','sdate']
}
</script>