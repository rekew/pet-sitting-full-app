<template>
    <section class="three">
        <h1 class="three-heading">Доверьте заботу о питомце профессионалам!</h1>
        <div class="buttons">
            <button>Зарегистрироваться</button>
            <button @click="googleForms">Google forms</button>
        </div>
        <footer>
            <div class="footer-contacts">
                <div class="footer-contacts-el">
                    <img class="location" src="@/assets/location-dot-solid.svg" alt="">
                    <h1>Алматы</h1>
                </div>
                <div class="footer-contacts-el">
                    <img class="phone" src="@/assets/phone-solid.svg" alt="">
                    <a href = "tel:+77770296982">+7 (777) - 029 - 6982</a>
                </div>
                <div class="footer-contacts-el">
                    <img class="email" src="@/assets/envelope-solid.svg" alt="">
                    <h1>anara.arman2019@gmail.com</h1>
                </div>
            </div>
            <div class="about-us-footer">
                <h1>Про Нас</h1>
                <p>Nanny – забота о вашем <br> питомце в надежных руках.</p>
            </div>
        </footer>
    </section>
</template>

<script>
export default {
    name: "SectionThree",
    methods:{
        googleForms(){
            window.location.href = 'https://docs.google.com/forms/d/e/1FAIpQLSfTcU90YGG1l3L77U6t41FsKUy-hwopANwO02ZnUt7DUFZdBQ/viewform?usp=dialog';
        }
    }
};
</script>

<style>
.three {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    background-color: #efd85d;
    padding: 20px;
    text-align: center;
}

.three-heading {
    font-family: 'Caveat', sans-serif;
    font-size: 50px;
    padding-top: 40px;
}

.buttons {
    padding-top: 40px;
}

.three button {
    cursor: pointer;
    font-family: "Roboto", sans-serif;
    color: #fff;
    font-size: 24px;
    width: 300px;
    height: 60px;
    font-weight: 600;
    border: solid white 2px;
    border-radius: 12px;
    background-color: #ff914d;
    transition: 0.3s;
}

.three button:hover {
    background-color: #ff7f2a;
}

.three footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 350px;
    width: 100%;
    margin-top: auto;
    padding: 40px 80px;
}

.footer-contacts {
    display: flex;
    flex-direction: column;
    gap: 40px;
}

.footer-contacts-el {
    display: flex;
    align-items: center;
    gap: 15px;
}

.footer-contacts-el h1 {
    font-family: 'Montserrat', sans-serif;
    font-size: 30px;
    font-weight: 300;
}

.footer-contacts-el a{
    font-family: 'Montserrat', sans-serif;
    font-size: 30px;
    font-weight: 300;
}

.about-us-footer {
    font-size: 30px;
    font-family: 'Caveat';
    display: flex;
    flex-direction: column;
    gap: 20px;
    text-align: left;
}

.location {
    width: 30px;
}
.phone {
    width: 37px;
}
.email {
    width: 35px;
}

@media (max-width: 1024px) {
    .three-heading {
        font-size: 40px;
    }

    .three button {
        width: 250px;
        height: 55px;
        font-size: 22px;
    }

    .three footer {
        flex-direction: column;
        height: auto;
        gap: 40px;
        padding: 30px 40px;
        text-align: center;
    }

    .footer-contacts,
    .about-us-footer {
        margin: 0;
        text-align: center;
    }

    .footer-contacts-el h1 {
        font-size: 26px;
    }
    
    .footer-contacts-el a {
        font-size: 26px;
    }

    .about-us-footer {
        font-size: 26px;
    }
}

@media (max-width: 768px) {
    .three-heading {
        font-size: 32px;
        padding-top: 20px;
    }

    .three button {
        width: 220px;
        height: 50px;
        font-size: 20px;
    }

    .three footer {
        flex-direction: column;
        height: auto;
        gap: 30px;
        padding: 20px;
    }

    .footer-contacts {
        gap: 25px;
    }

    .footer-contacts-el {
        flex-direction: column;
        gap: 10px;
    }

    .footer-contacts-el h1 {
        font-size: 22px;
    }

    .footer-contacts-el a {
        font-size: 22px;
    }

    .about-us-footer {
        font-size: 22px;
        text-align: center;
    }

    .location,
    .phone,
    .email {
        width: 28px;
    }
}

@media (max-width: 480px) {
    .three-heading {
        font-size: 28px;
    }

    .three button {
        width: 200px;
        height: 45px;
        font-size: 18px;
    }

    .footer-contacts-el h1 {
        font-size: 18px;
    }
    .footer-contacts-el a {
        font-size: 18px;
    }

    .about-us-footer {
        font-size: 18px;
    }

    .location,
    .phone,
    .email {
        width: 25px;
    }
}

@media (min-width: 1440px) {
    .three-heading {
        font-size: 55px;
    }

    .three button {
        width: 300px;
        height: 65px;
        font-size: 26px;
    }

    .footer-contacts-el h1 {
        font-size: 35px;
    }
    
    .footer-contacts-el a {
        font-size: 35px;
    }

    .about-us-footer {
        font-size: 35px;
    }

    .about-us-footer h1{
        font-size: 60px;
    }

    .location,
    .phone,
    .email {
        width: 40px;
    }
}

@media (min-width: 2000px) {
    .three-heading {
        font-size: 70px;
    }

    .three button {
        width: 400px;
        height: 80px;
        font-size: 35px;
    }

    .footer-contacts-el h1 {
        font-size: 50px;
    }
    
    .footer-contacts-el a {
        font-size: 50px;
    }

    .about-us-footer {
        font-size: 60px;
    }

    .about-us-footer h1{
        font-size: 80px;
    }

    .location,
    .phone,
    .email {
        width: 60px;
    }
}


</style>
