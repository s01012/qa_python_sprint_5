link_account_button = '//p[text()="Личный Кабинет"]/parent::a'  # Ссылка на личный кабинет

checkout_button = '//div/button[text()="Оформить заказ"]' #Кнопка оформить заказ

link_enter = './/div/button[text()="Войти в аккаунт"]'  # Ссылка на форму Войти в аккаунт

link_sign_up = './/a[text()="Зарегистрироваться"]'  # Ссылка на форму регистрации пользователя

name_input_registration_form = '//div[h2[text()="Регистрация"]]/descendant::label[text()="Имя"]/following-sibling::input'  # Поле ввода Имя в форме регистрации

email_input_registration_form = '//div[h2[text()="Регистрация"]]/descendant::label[text()="Email"]/following-sibling::input'  # Поле ввода эл.почты в форме регистрации

password_input_registration_form = '//div[h2[text()="Регистрация"]]/descendant::label[text()="Пароль"]/following-sibling::input'  # Поле ввода Пароль в форме регистрации

registration_button_registration_form = './/form[contains(@class, "Auth_form")]/button[text()="Зарегистрироваться"]'  # Кнопка зарегистрироваться в форме регистрации

enter_button_registration_form = '//p[text()="Уже зарегистрированы?"]/a[text()="Войти"]'  # Ссылка на форму авторизации в форме регистрации

enter_button_restore_form = '//p[text()="Вспомнили пароль?"]/a[text()="Войти"]'  # Ссылка на форму авторизации в форме восстановления пароля

restore_password_button = '//p[text()="Забыли пароль?"]/a[text()="Восстановить пароль"]'  # Ссыька на форму восстановления пароля

incorrect_password_message = './/p[text()="Некорректный пароль"]'  # Сообщение о некорректном пароле

email_input_authorization_form = '//div[h2[text()="Вход"]]/descendant::label[text()="Email"]/following-sibling::input'  # Поле ввода эл.почты в форме авторизации

password_input_authorization_form = '//div[h2[text()="Вход"]]/descendant::label[text()="Пароль"]/following-sibling::input'  # Поле ввода пароля в форме авторизации

authorization_button_authorization_form = './/form[@class="Auth_form__3qKeq mb-20"]/button[text()="Войти"]'  # Кнопка войти в форме авторизации

personal_input_login = './/descendant::label[text()="Логин"]/following-sibling::input[1]'  # Поле с информацией о логине в личном кабинете

link_constractor = '//p[text()="Конструктор"]/parent::a'  # Ссылка на конструктор

exit_button = '//button[text()="Выход"]'  # Кнопка выхода из авторизованного состояния

link_constractor_sauce = '//span[text()="Соусы"]/parent::div'  # Ссылка на раздел соусы

link_constractor_bun = '//span[text()="Булки"]/parent::div'  # Ссылка на раздел булки

link_constractor_filling = '//span[text()="Начинки"]/parent::div'  # Ссылка на раздел начинки
