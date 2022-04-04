<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
           Welcome to <b><i> Memories </i></b>
          </h1>
          <h2 class="subtitle">
            Place to store your nice<b><i> Memories </i></b>
          </h2>
        </div>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Memories</h2>
      </div>

      <div
        class="column is-3"
        v-for="memory in latestMemories"
        v-bind:key="memory.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="memory.get_photo">
          </figure>

          <h3 class="is-size-4">{{ memory.name }}</h3>
          <p class="is-size-6"><b>Species: </b>{{ memory.species }}</p>
          <p class="is-size-6"><b>Weight: </b>{{ memory.weight }} kg</p>
          <p class="is-size-6"><b>Length of fish: </b>{{ memory.length }} cm</p>
          <p class="is-size-6"><b>Timestamp: </b>on {{ memory.timestamp.replace("T", " at ").replace("Z", "") }}</p>
          <p class="is-size-6"><b>Location where caught (Coordinates): </b>{{ memory.latitude }}° N, {{ memory.longitude }}° E</p>
          <p class="is-size-6"><b>Fish description: </b>{{ memory.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      latestMemories: [],
    }
  },
  components: {
  },
  mounted() {
    this.getLatestMemories()

    document.title = 'Home - Memories'
  },
  methods: {
    getLatestMemories() {
      axios.get('/api/v1/latest-memories/')
        .then(response => {
          this.latestMemories = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>