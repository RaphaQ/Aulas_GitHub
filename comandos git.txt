#para ver se tem um github conectado
git config --global user.name 
git config --global user.email 



#caso tenha um github conectado, 
para desconectar:
git config --global --unset user.name
git config --global --unset user.email



#para conectar o seu github:
git config --global user.name "nome de usuario"
git config --global user.email "email do github"


#para verificar se realmente conectou a sua conta:
git config --global user.name


-------------------------- começa aqui _____________________

#para dar permissão ao git 
#de manipular os códigos que estão na pasta
git init

#para conectar a pasta remota (pasta do github) com a pasta
#local (pasta do computador)
git remote add origin link-do-repositorio

#para ver em quais arquivos eu ja dei ok:
git status - Inicialmente aparece tudo vermelho

#para dar ok em todos os arquivos:
git add .

#para configurar uma frase de commit:
git commit -m "frase do commit" (geralmente 
é a ultima coisa que voce fez nessa nova versão)

#para empurrar os arquivos da máquina local, para a pasa remota:
git push origin master