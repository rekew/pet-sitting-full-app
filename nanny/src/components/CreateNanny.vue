<template>
  <div class="be-nanny">
    <div class="form-box">
      <form class="form" @submit.prevent="submitApplication">
        <span class="title">Стать няней для питомцев</span>
        <span class="subtitle">Заполните форму, чтобы подать заявку</span>

        <div class="form-container">
          <input
            type="text"
            class="input"
            v-model="form.fullName"
            placeholder="Ваше имя"
            required
          />
          <input
            type="email"
            class="input"
            v-model="form.email"
            placeholder="Email"
            required
          />
          <input
            type="tel"
            class="input"
            v-model="form.phone"
            placeholder="Телефон"
            required
          />
          <textarea
            class="input"
            v-model="form.experience"
            placeholder="Опыт ухода за животными"
            rows="4"
          ></textarea>
          <select class="input" v-model="form.petTypes" multiple>
            <option disabled>Типы животных</option>
            <option value="dogs">Собаки</option>
            <option value="cats">Кошки</option>
            <option value="birds">Птицы</option>
            <option value="other">Другие</option>
          </select>
          <input
            type="text"
            class="input"
            v-model="form.availability"
            placeholder="Доступность / Расписание"
          />
        </div>

        <button type="submit">Подать заявку</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateNanny",
  data() {
    return {
      form: {
        fullName: "",
        email: "",
        phone: "",
        experience: "",
        petTypes: [],
        availability: "",
      },
    };
  },
};
</script>

<style scoped>
.be-nanny {
  font-family: "Montserrat", sans-serif;
  background-color: #efd85d;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  box-sizing: border-box;
}

.form-box {
  background: white;
  padding: 30px;
  border-radius: 10px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.form {
  display: flex;
  flex-direction: column;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
  text-align: center;
}

.subtitle {
  font-size: 16px;
  margin-bottom: 20px;
  color: #666;
  text-align: center;
}

.form-container {
  display: flex;
  flex-direction: column;
}

.input {
  margin-bottom: 15px;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

textarea.input {
  resize: vertical;
}

select.input {
  height: auto;
}

button {
  background-color: #f9c846;
  border: none;
  padding: 12px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #e0b43d;
}

/* ✅ Responsive Design */

/* Tablets (portrait and up) */
@media (max-width: 768px) {
  .form-box {
    padding: 25px;
  }

  .title {
    font-size: 22px;
  }

  .subtitle {
    font-size: 15px;
  }

  .input {
    font-size: 13px;
    padding: 9px;
  }

  button {
    font-size: 15px;
    padding: 10px;
  }
}

/* Phones */
@media (max-width: 480px) {
  .form-box {
    padding: 20px;
  }

  .title {
    font-size: 20px;
  }

  .subtitle {
    font-size: 14px;
  }

  .input {
    font-size: 12px;
    padding: 8px;
  }

  button {
    font-size: 14px;
    padding: 10px;
  }
}
</style>
