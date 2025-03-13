<template>
    <div class = 'registerPage'>
        <div class="form-box">
            <form class="form">
                <span class="title">Зарегистрироваться</span>
                <span class="subtitle">Создайте бесплатный аккаунт с вашим email-ом</span>
                <div class="form-container">
                    <input type="text" class="input" placeholder="ФИО">
                    <input type="email" class="input" placeholder="Email">
                    <input type="password" class="input" placeholder="Пароль">
                </div>
                <button>Зарегистрироваться</button>
            </form>
            <div class="form-section">
                <p>Уже есть Аккант? 
                    <router-link to="/login">
                        <a>Войти</a> 
                    </router-link>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name : 'RegisterPage',
    components : {
        
    }
}
</script>

<style>
    .registerPage{
        font-family: 'Montserrat', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 10px;
        min-height: 100vh;
        background-color: #ffde59;
    }

.form-box {
  max-width: 300px;
  background: #f1f7fe;
  overflow: hidden;
  border-radius: 16px;
  color: #010101;
}

.form {
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 32px 24px 24px;
  gap: 16px;
  text-align: center;
}
.title {
  font-weight: bold;
  font-size: 1.2rem;
}

.subtitle {
  font-size: 1rem;
  color: #666;
}

.form-container {
  overflow: hidden;
  border-radius: 8px;
  background-color: #fff;
  margin: 1rem 0 .5rem;
  width: 100%;
}

.input {
  background: none;
  border: 0;
  outline: 0;
  height: 40px;
  width: 100%;
  border-bottom: 1px solid #eee;
  font-size: .9rem;
  padding: 8px 15px;
}

.form-section {
  padding: 16px;
  font-size: .85rem;
  background-color: #e0ecfb;
  box-shadow: rgb(0 0 0 / 8%) 0 -1px;
}

.form-section a {
  font-weight: bold;
  color: #0066ff;
  transition: color .3s ease;
}

.form-section a:hover {
  color: #005ce6;
  text-decoration: underline;
}

.form button {
  background-color: #0066ff;
  color: #fff;
  border: 0;
  border-radius: 24px;
  padding: 10px 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color .3s ease;
}

.form button:hover {
  background-color: #005ce6;
}
</style>