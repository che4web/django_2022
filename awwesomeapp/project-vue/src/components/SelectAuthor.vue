<template> 
    <v-select @search="getAuhtor" :options="authorList" label="name" @update:modelValue="$emit('update:modelValue',$event)"/>

</template>
<script>
import vSelect from "vue-select"
import axios from 'axios'
export default{
    name:"select-author",
    props:['modelValue'],
    components:{
        vSelect,
    },
    data(){
        return {
            authorName:'',
            authorList:[],
        }
    },
    methods:{
        async getAuhtor(search){
            let   params={name__icontains:search}
            let data =  (await axios.get('/api/author/',{params})).data
            this.authorList = data
        },


    }
}
</script>
