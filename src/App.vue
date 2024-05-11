
<template>
    <Person></Person>
</template>

<script>
 import Person from "./components/Person.vue"

 export default {
    name: 'App',
    components:{
        Person
    }
 }
</script>

<style>
    .app{
        background-color: grey;
        box-shadow: 0 0 10px;
        border-radius: 10px;
        padding: 20px;
    }
</style>