<template>
  <nav>
    <div class="top">
      <div class="first">
        <img src="@/assets/logo.svg" alt="Логотип" />
        <h1>Nanny</h1>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style>
nav {
  width: 100%;
}
.top {
  padding: 0 40px;
  background-color: #ff914d;
  display: flex;
  align-items: center;
}
.first {
  display: flex;
  align-items: center;
  gap: 40px;
  padding: 30px 0;
  height: 120px;
}
.first h1 {
  font-size: 100px;
  color: white;
  font-family: lumios-marker, sans-serif;
}
.first img {
  transform: rotate(-5deg);
  width: 100px;
}

@media (max-width: 1024px) {
  .first h1 {
    font-size: 60px;
  }
  .first img {
    width: 80px;
  }
}

@media (max-width: 768px) {
  .first h1 {
    font-size: 40px;
  }
  .first img {
    width: 60px;
  }
}
</style>
