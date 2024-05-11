
<template>
    <div class="person">
        <h2>一辆{{car.brand}}车，价格{{car.price}}</h2>
        <button @click="updatePrice">update car's price</button>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { reactive } from 'vue';
    let car = reactive({brand: 'benz', price:100})
    console.log(car)
    function updatePrice(){
        car.price += 200
    }
</script>


<style scoped>
.person{
    background-color: skyblue;
    box-shadow: 0 0 10px;
    border-radius: 10px;
    padding: 20px;
}
</style>