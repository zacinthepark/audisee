<template>
  <div>
    <p>{{ music.track_name }}</p>
    <!-- 플레이리스트 추가 실험용 버튼 -->
    <button @click="addToMyTrack">add to playlist</button>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "MainAItem",
  // movie 프롭 받아놓음
  props: {
    movie: Object,
    music: Object,
  },
  methods: {
    addToMyTrack() {
      const track_genre = this.music.track_genre
      const track_name = this.music.track_name
      const artist_name = this.music.artist_name
      const album_name = this.music.album_name
      const cover_path = this.music.cover_path
      const preview_url = this.music.preview_url
      axios({
        method: 'post',
        url: `${API_URL}/playlist/tracks/`,
        data: {
          track_genre: track_genre,
          track_name: track_name,
          artist_name: artist_name,
          album_name: album_name,
          cover_path: cover_path,
          preview_url: preview_url,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
};
</script>

<style></style>
