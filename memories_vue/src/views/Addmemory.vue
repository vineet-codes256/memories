<template>
  <div class="home">
    <section class="hero is-primary is-small mb-6">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
           Add new Adventure <b><i> Memories </i></b>
          </h1>
          <h2 class="subtitle">
            Store your new<b><i> Memories </i></b>
          </h2>
        </div>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Create Memories</h2>
      </div>

      <div class="column is-12">
        <form action="{{ route('memories.store') }}" method="POST" enctype="multipart/form-data">
          @csrf
          <div class="field">
            <label class="label">Name</label>
            <div class="control">
              <input class="input" type="text" name="name" placeholder="Name" required>
            </div>
          </div>
          
          <div class="field">
            <label class="label">Species</label>
            <div class="control">
              <input class="input" type="text" name="species" placeholder="Species" required>
            </div>
          </div>

          <div class="field">
            <label class="label">Weight</label>
            <div class="control">
              <input class="input" type="float" name="weight" placeholder="Weight" required>
            </div>
          </div>

          <div class="field">
            <label class="label">Length</label>
            <div class="control">
              <input class="input" type="float" name="length" placeholder="Length" required>
            </div>
          </div>

          <div class="field">
            <label class="label">Latitude</label>
            <div class="control">
              <input class="input" type="float" name="latitude" placeholder="Latitude" required>
            </div>
          </div>

          <div class="field">
            <label class="label">Longitude</label>
            <div class="control">
              <input class="input" type="float" name="longitude" placeholder="Longitude" required>
            </div>
          </div>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <textarea class="textfield" name="description" placeholder="Description" required></textarea>
            </div>
          </div>

          <div class="field">
            <label class="label">Timestamp</label>
            <div class="control">
              <input class="input" type="datetime-local" name="timestamp" placeholder="Timestamp" required>
            </div>
          </div>

          <div class="field">
            <label class="label">Photo</label>
            <div class="control">
              <input class="input" type="file" name="image" required>
            </div>
          </div>
        </form>
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