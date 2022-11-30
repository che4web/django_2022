<template>
    <div>
        Описание статьи
        <h2>{{article.name}} {{article.id}}</h2>
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
