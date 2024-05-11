
<template>
    <div class="person">
        <h3>name:{{name}}</h3>
        <h3>age:{{age}}</h3>
        <button @click="showTel">show tel</button>
        <button @click="changeName">update name</button>
        <button @click="changeAge">update age</button>

    </div>
</template>

<!-- <script>
 export default {
    name: 'Person',
    setup(){
        let name = '张三'
        let age = "18"
        let tel = "123341313"

        function showTel(){
            alert(tel)
        }

        function changeAge(){
            age++
        }

        function changeName(){
            name="哈哈哈哈"
        }

        return {name, age, tel, showTel, changeAge, changeName}
        // return ()=>"哈哈"
    }
 }
</script> -->
<script>
 export default {
     name: 'Person',
    }
</script>
<script setup name="Person1234">
    import { ref } from 'vue';

    let name = ref('张三')
    let age = ref("18")
    let tel = "123341313"
    console.log(name)
    console.log(age)
    console.log(tel)

    function showTel(){
        alert(tel)
    }

    function changeAge(){
        age.value++
    }

    function changeName(){
        name.value="哈哈哈哈"
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