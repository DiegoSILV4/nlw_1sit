from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurando o driver do navegador (necessário ter o ChromeDriver instalado)
driver = webdriver.Chrome()

try:
    # Acesse o site do jogo
    driver.get("https://www.edergrau.me/compra/67598a64eb778483220241211")

    # Aguarde a página carregar
    time.sleep(3)

    # Interaja com o site (exemplo: encontre um campo para inserir números)
    input_field = driver.find_element(By.ID, "campo_de_numero")
    input_field.send_keys("8628555")  # Insira o número desejado

    # Envie o número
    input_field.send_keys(Keys.RETURN)

    # Aguarde um pouco para observar o resultado
    time.sleep(5)
finally:
    # Feche o navegador
    driver.quit()
