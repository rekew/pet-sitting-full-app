<template>
    <div class="top-section-two">
        <img src="@/assets/section-two.png" alt="">
        <h1>Почему мы?</h1>
    </div>

    <section class="two">
        <div class="list-of-items">
            <div v-for="(feature, index) in features" :key="index" class="feature-item">
                <div class="itemss">
                    <img src="@/assets/paw-section-two.png" alt="icon" class="feature-icon">
                    <span class="feature-text">{{ feature.text }}</span>
                </div>
                <div class="line"></div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "SectionTwo",
    data() {
        return {
            features: [
                { text: 'Проверенные и сертифицированные няни' },
                { text: 'Удобный поиск и бронирование' },
                { text: 'Круглосуточная поддержка' },
                { text: 'Безопасные встречи и страхование' },
                { text: 'Проверка нянь через собеседование' },
                { text: 'Индивидуальный подход к каждому питомцу' },
                { text: 'Фото и видеоотчеты о проведенном времени с питомцем' },
                { text: 'Гибкий график (доступность няни в любое время)' },
                { text: 'Доступные цены и прозрачная система оплаты' },
                { text: 'Бронируете онлайн и оплачиваете' }
            ]
        };
    }
};
</script>

<style>
.two {
    min-height: 100vh;
    background: url('@/assets/section-two-back.png') no-repeat center center;
    background-size: cover;
    padding: 50px 20px;
}

.top-section-two h1{
    width: 330px;
}

.list-of-items {
    display: flex;
    flex-direction: column;
    gap: 20px; 
    width: 80%;
    max-width: 800px;
}

.feature-item {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 20px; 
}

.itemss {
    display: flex;
    align-items: center;
    gap: 15px; 
}

.feature-icon {
    width: 40px;
}

.feature-text {
    font-size: 25px;
    font-family: 'Montserrat', sans-serif;
    color: #483932;
}

@media (max-width: 1024px) {
    .feature-text {
        font-size: 22px;
    }
}

@media (max-width: 768px) {
    .feature-text {
        font-size: 20px;
    }
}

@media (max-width: 480px) {
    .feature-text {
        font-size: 18px;
    }
}

.line {
    height: 2px;
    background-color: #ddd;
    flex-grow: 1; 
}

.top-section-two {
    color: white;
    display: flex;
    align-items: center;
    font-family: 'Caveat', sans-serif;
    background-color: #ffde59;
    gap: 20px;
    padding: 15px;
}

.top-section-two img {
    padding: 10px 0;
    margin-left: 40px;
    width: 110px;
    opacity: 0.7;
}

.top-section-two h1 {
    font-size: 70px;
    color: white;
}

@media (min-width : 1440px){
    .top-section-two h1{
        width: 400px;
        height: 120px;
        font-size: 80px;
    }
    .feature-text{
        font-size: 30px;
    }
}

@media (min-width : 2000px){
    .top-section-two h1{
        width: 500px;
        height: 140px;
        font-size: 100px;
    }
    .feature-text{
        font-size: 40px;
    }
}

</style>
