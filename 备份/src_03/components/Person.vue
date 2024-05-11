
<template>
    <div class="person">
        <h3>name:{{name}}</h3>
        <h3>age:{{age}}</h3>
        <button @click="showTel">show tel</button>
        <button @click="changeName">update name</button>
        <button @click="changeAge">update age</button>

    </div>
</template>

<script>
 export default {
    name: 'Person',
    // data(){
    //     return {
    //         name: '张三',
    //         age: "18",
    //         tel: "123341313"
    //     }
    // },
    // methods:{
    //     showTel(){
    //         alert(this.tel)
    //     },
    //     changeAge(){
    //         this.age++
    //     },
    //     changeName(){
    //         this.name="哈哈哈哈"
    //     }
    // },
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
    }
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