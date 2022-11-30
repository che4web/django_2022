<template> 
    <v-select @search="getAuhtor" :options="authorList" label="name" @update:modelValue="$emit('update:modelValue',$event)"/>

</template>
<script>
import vSelect from "vue-select"
import {Author} from "@/api"
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
            let data = await Author.objects.filter(params)
            this.authorList = data.results
        },


    }
}
</script>
