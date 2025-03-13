<template>
    <NavBar />
    <SectionOne />
    <SectionTwo />
    <SectionThree />
  </template>
  
  <script>
  import NavBar from '@/components/NavBar.vue';
  import SectionOne from '@/components/Section-one.vue';
  import SectionTwo from '@/components/Section-two.vue';
  import SectionThree from '@/components/Section-three.vue';
  
  export default {
    name: 'HomePage',
    components: {
      NavBar,
      SectionOne,
      SectionTwo,
      SectionThree,
    }
  };
  </script>
  