<template>
  <div class="pl-5 pr-5" style="padding-top: 80px;">
    <Calendar v-for="c in calendars" :key="c.name" :name="c.name" />
  </div>
</template>

<script>
import Calendar from '@/components/Calendar.vue';

export default {
  data() {
    return {
      calendars: []
    }
  },
  components: {
    Calendar
  },
  mounted() {
    this.$google.getCalendars().then(c => {
      this.calendars = c.map(v => ({
        name: v.summary.slice(12)
      }));
    });

    // this.$google.createCalendar("Calender test");

  }
}
</script>

<style lang="scss">
.content {
  margin-left: 160px;
  padding-top: 55px;
}
</style>