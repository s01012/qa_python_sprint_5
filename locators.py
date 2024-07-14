# link_account_button = './/a[@class="AppHeader_header__link__3D_hX" and @href="/account"]/p[text()="Личный Кабинет"]'
link_account_button = '//p[text()="Личный Кабинет"]/parent::a'
link_enter = './/div/button[text()="Войти в аккаунт"]'

link_sign_up = './/a[text()="Зарегистрироваться"]'

name_input_registration_form = '//div[h2[text()="Регистрация"]]/descendant::label[text()="Имя"]/following-sibling::input'

email_input_registration_form = '//div[h2[text()="Регистрация"]]/descendant::label[text()="Email"]/following-sibling::input'
# .//label[text()="Имя"]/following-sibling::input

password_input_registration_form = '//div[h2[text()="Регистрация"]]/descendant::label[text()="Пароль"]/following-sibling::input'

registration_button_registration_form = './/form[@class="Auth_form__3qKeq mb-20"]/button[text()="Зарегистрироваться"]'

enter_button_registration_form = '//p[text()="Уже зарегистрированы?"]/a[text()="Войти"]'

enter_button_restore_form = '//p[text()="Вспомнили пароль?"]/a[text()="Войти"]'

restore_password_button = '//p[text()="Забыли пароль?"]/a[text()="Восстановить пароль"]'

incorrect_password_message = './/p[text()="Некорректный пароль"]'

email_input_authorization_form = '//div[h2[text()="Вход"]]/descendant::label[text()="Email"]/following-sibling::input'

password_input_authorization_form = '//div[h2[text()="Вход"]]/descendant::label[text()="Пароль"]/following-sibling::input'

authorization_button_authorization_form = './/form[@class="Auth_form__3qKeq mb-20"]/button[text()="Войти"]'

personal_input_login = './/descendant::label[text()="Логин"]/following-sibling::input[1]'

link_constractor = '//p[text()="Конструктор"]/parent::a'

exit_button = '//button[text()="Выход"]'

link_constractor_sauce = '//span[text()="Соусы"]/parent::div'

link_constractor_bun = '//span[text()="Булки"]/parent::div'

link_constractor_filling = '//span[text()="Начинки"]/parent::div'
