<template>
    <nav>
        <div class="top">
            <div class="first">
                <img src="@/assets/logo.svg" alt="Логотип">
                <h1>Nanny</h1>
            </div>
            <div class="second">
                <router-link to="/register">
                    <img src="@/assets/user.svg" alt="Профиль" class="user-icon">
                </router-link>

                <button class="burger" @click="toggleMenu">
                    ☰
                </button>
            </div>
        </div>
        <div class="bottom" :class="{ 'active': isMenuOpen }">
            <ul>
                <li><a href="#">Поиск няни</a></li>
                <li><a href="#">Карта мест</a></li>
                <li><a href="#">Груминг</a></li>
                <li><a href="#">Как это работает</a></li>
                <li><a href="#">Контакты</a></li>
                <li class="register"><a href="#">Зарегистрироваться</a></li>
            </ul>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavBar",
    data() {
        return {
            isMenuOpen: false
        };
    },
    methods: {
        toggleMenu() {
            this.isMenuOpen = !this.isMenuOpen;
        }
    }
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
.second {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 20px;
}
.user-icon {
    cursor: pointer;
    width: 80px;
}

.burger {
    display: none;
    font-size: 40px;
    background: none;
    border: none;
    color: white;
    cursor: pointer;
}

.bottom {
    background-color: #ffde59;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease-in-out;
}
.bottom ul {
    display: flex;
    gap: 56px;
}
.bottom a {
    color: #f07022;
    font-size: 30px;
    font-family: 'Roboto', sans-serif;
}

.register {
    display: none;
}

@media (max-width: 1024px) {
    .first h1 {
        font-size: 60px;
    }
    .first img {
        width: 80px;
    }
    .user-icon {
        width: 60px;
    }
    .bottom a {
        font-size: 24px;
    }
}

@media (max-width: 768px) {
    .first h1 {
        font-size: 40px;
    }
    .first img {
        width: 60px;
    }
    .burger {
        display: block;
    }
    .user-icon {
        display: none;
    }
    .bottom {
        height: 0;
        overflow: hidden;
        flex-direction: column;
        padding: 0;
    }
    .bottom ul {
        flex-direction: column;
        gap: 20px;
        text-align: center;
        padding: 20px;
    }
    .bottom.active {
        height: auto;
        padding: 20px 0;
    }

   
    .register {
        display: block;
    }
}
</style>
