<template>
  <section class="one">
    <div class="content">
      <img class="section-one-text" src="@/assets/section-one-text.svg" alt="">
      <div class="buttons">
        <button>Найти няню</button>
        <button>Стать няней</button>
      </div>
    </div>
    <h1 class="section-one-footer-text">
      Найдите заботливую няню для вашего питомца в один клик!
    </h1>
  </section>
</template>

<script>
export default {
  name: "SectionOne",
};
</script>

<style>
.one {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 100vh;
  background: url("@/assets/Nanny.png") no-repeat center top / cover;
  color: white;
  padding: 10px;
  text-align: center;
}

.content {
  display: flex;
  justify-content: space-between; 
  align-items: center;
  width: 100%;
  max-width: 1200px;
}

.main-text {
  background: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
  font-family: "Caveat", sans-serif;
  font-size: 50px;
  font-weight: 400;
  flex: 1; 
  text-align: left;
  max-width: 900px;
}

.section-one-text {
  width: 100%;
  max-width: 700px; 
  height: auto;
}

.buttons {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.buttons button {
  cursor: pointer;
  font-family: "Roboto", sans-serif;
  color: #fff;
  font-size: 24px;
  width: 200px;
  height: 60px;
  font-weight: 600;
  border: solid white 2px;
  border-radius: 12px;
  background-color: #ff914d;
  transition: 0.3s;
}

.buttons button:hover {
  background-color: #ff7a30;
}

.section-one-footer-text {
  font-weight: 600;
  font-size: 40px;
  width: 100%;
  max-width: 1200px;
  padding-bottom: 20px;
  text-align: center;
  padding: 15px;
  font-family: 'Caveat', sans-serif;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
}

@media (min-width: 2000px) {
  .content {
    max-width: 2200px;
  }
  .section-one-text {
    max-width: 1200px;
  }
  .buttons {
    flex-direction: row;
    gap: 30px;
  }
  .buttons button {
    width: 320px;
    height: 90px;
    font-size: 34px;
  }
  .section-one-footer-text {
    font-size: 60px;
  }
}

@media (min-width: 1440px) {
  .content {
    max-width: 1500px;
  }
  .section-one-text {
    max-width: 750px;
  }
  .buttons {
    gap: 20px;
  }
  .buttons button {
    width: 250px;
    height: 75px;
    font-size: 30px;
  }
  .section-one-footer-text {
    font-size: 55px;
  }
}

@media (max-width: 1024px) {
  .content {
      flex-direction: column;
      text-align: center;
  }
  .main-text {
      max-width: 700px;
      font-size: 40px;
      text-align: center;
  }
  .buttons {
      flex-direction: row;
      justify-content: center;
      gap: 10px;
  }
  .buttons button {
      width: 190px;
      height: 55px;
      font-size: 22px;
  }
  .section-one-text {
      max-width: 600px; 
  }
}

@media (max-width: 768px) {
  .content {
      flex-direction: column;
      text-align: center;
  }
  .main-text {
      max-width: 90%;
      font-size: 30px;
      text-align: center;
  }
  .buttons {
      flex-direction: column;
      align-items: center;
      gap: 15px;
  }
  .buttons button {
      width: 180px;
      height: 50px;
      font-size: 20px;
  }
  .section-one-footer-text {
      font-size: 28px;
      padding: 10px;
  }
  .section-one-text {
      max-width: 500px; 
  }
}

@media (max-width: 480px) {
  .buttons {
      flex-direction: column;
      align-items: center;
      gap: 10px;
  }
  .buttons button {
      width: 160px;
      height: 45px;
      font-size: 18px;
  }
  .section-one-text {
      max-width: 400px; 
  }
}
</style>
