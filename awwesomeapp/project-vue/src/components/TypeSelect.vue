<template> 
    <v-select @search="getJournal" :options="authorList" label="name" @update:modelValue="$emit('update:modelValue',$event)"/>

</template>
<script>
import vSelect from "vue-select"
import axios from 'axios'
export default{
    name:"select-type",
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
    mounted(){
        this.getJournal()
    },
    methods:{
        async getJournal(search){
            let   params={name__icontains:search}
            let data =  (await axios.get('/api/type/',{params})).data
            this.authorList = data.results
        },


    }
}
</script>
