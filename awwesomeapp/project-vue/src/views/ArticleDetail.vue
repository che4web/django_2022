<template>
    <div>
        Описание статьи
        <h2>{{article.name}} {{article.id}}</h2>
        <h2>Дополнительна информация</h2>
        <div v-for="val,key in article.addition_info" :key="key">
            <b>{{key}}</b> {{val}}
            </div>
    </div>
</template>
<script>
import {Article} from "@/api"
export default {
    name:"article-detail",
    data(){
        return {
            article:{}
        }
    },
    methods:{
        async getArticle(){
        const id = this.$route.params.id
        this.article = await Article.objects.get(id)

        }
    },

    mounted(){
        this.getArticle()
    }
}
</script>
