<template>
    <div>
        Описание Журнала
        <h2>{{journal.name}} {{journal.id}}</h2>
    </div>
    <div v-for="a in articleList" :key="a.id">{{a.name}}</div>
</template>
<script>
import {Journal,Article} from "@/api"
export default {
    name:"journal-detail",
    data(){
        return {
            journal:{},
            articleList:[],
        }
    },
    methods:{
        async getJournal(){
        const id = this.$route.params.id
        this.journal= await Journal.objects.get(id)
        this.articleList = await Article.objects.filter({journal:id})

        }
    },

    mounted(){
        this.getJournal()
    }
}
</script>
