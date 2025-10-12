<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { posts } from '../components/posts.js'

const route = useRoute()
const id = Number(route.params.id)
const post = posts.find(p => p.id === id)

const comments = ref([])
const showComments = ref(false)

const likes = ref([])
const showLikes = ref(false)

async function fetchComments() {
  if (!showComments.value) {
    const res = await fetch(`http://localhost:8000/api/comments/${id}`)
    comments.value = await res.json()
    showComments.value = true
  } else {
    showComments.value = false
  }
}

async function fetchLikes(){
        const res = await fetch(`http://localhost:8000/api/likes/${id}`)
        likes.value = await res.json()
}

function toggleShowLikes() {
    showLikes.value = !showLikes.value
}

onMounted(() => {
  fetchLikes()
})
</script>

<template>
    <div class="flex justify-center mt-8">
        <article class="max-w-3xl  p-6">
          <h1 class="text-2xl font-bold">{{ post.title }}</h1>
          <p class="mt-1 text-sm">By {{ post.author }}</p>
          <p class="mt-4 leading-relaxed ">{{ post.excerpt }}{{ post.more }}</p>
         <img :src="post.image" alt="cover" class="w-full h-64 object-cover rounded mb-4 mt-3" />
          <div class="flex gap-4 my-4 ">
            <button @click="fetchComments" class="px-4 py-2 bg-blue-500 text-white rounded">
              {{ showComments ? '隱藏留言' : 'Comments' }}
            </button>
            <button @click="toggleShowLikes" class="px-4 py-2 bg-pink-500 text-white rounded">
                {{likes.length +' Likes'}}
            </button>
          </div>    
        </article>
        <div class="w-80 ml-8">
            <div v-show="showComments" class="mt-4 p-4 ">
                <p class="font-bold mb-2">Comments</p>
                <div v-for="(c, idx) in comments" :key="idx" class="m-2 border p-2 rounded">
                    <p>{{ c.content }}</p>
                    <small class="text-gray-500">By {{ c.author }}</small>
                </div>
            </div>
        
            <div v-show="showLikes" class="mt-4 p-4 rounded">
                <p class="font-bold mb-2">Likes</p>
                <div v-for="(c, idx) in likes" :key="idx" class="m-2 border p-2 rounded">
                    <p>{{ c.author }}</p>
                    <small class="text-pink-500">{{c.content }}</small>
                </div>
            </div>
        </div>
    </div>
</template>