<center>

# Associ'Action
</center>

## Badges
![Static Badge](https://img.shields.io/badge/Status-pre_deployment-green)
![Static Badge](https://img.shields.io/badge/Version-1.0.0-blue)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

---
## Description

### Associ'Action vous ouvre les portes d'une agora virtuelle, d'un marché dynamique des associations, vous permettant de découvrir, adhérer et profiter des services proposés par une multitude d'organisations. Interagissez, partagez des expériences et contribuez activement à la vie associative de votre communauté.
---
<center>

## Sommaire


[**Overall operation**](#Overall-operation)  

[**For Local Use**](#For-Local-Use)  

[**About me**](#About-me)  

[**Links**](#Links)

[**Tools**](#Tools)  

---
</center>
<center>

## Overall operation
</center>
<a name="Overall-operation"></a>
L'utilisateur peut effectuer des recherches d'associations via leurs noms ou leur ville d'implantation, il peut ensuite accéder à leur page détaillée qui leur permettra de voir les informations de celle-ci ainsi qu'accéder aux événements de cette dernière.

L'utilisateur peut aussi s'inscrire sur le site afin que ses informations soient enregistrées et facilitent la recherche géographique ou sectorielle des associations.

De plus, le fait de s'incrire permettra d'avoir son propre répertoire d'association et d'ainsi accéder aux évènements plus rapidement.

Si l'utilisateur est un membre de l'association, il existe trois catégories reconnues: adhérent, administrateur, directeur; chacun de ses rôles à des droits sur le précédent.

Bien entendu, le passage d'un membre au rôle de directeur d'association passe par une demande à l'administrateur de l'application via email.


---
## 🏠 For Local Use
<a name="For-Local-Use"></a>
Pour utiliser ce projet en local, suivez les étapes suivantes :

### 1. Téléchargement du Projet

Téléchargez le projet en cliquant sur le bouton "Code" en haut à droite de cette page, puis sélectionnez "Download ZIP".  
Décompressez ensuite le fichier ZIP téléchargé.

### 2. Vérification de la Version de Python

Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez vérifier la version de Python en utilisant la commande suivante :  

```bash
python --version
```

Assurez-vous d'avoir au moins Python 3.8 ou une version ultérieure.

### 3. Initialisation de l'Environnement Virtuel

Avant de commencer, créez un environnement virtuel en utilisant la commande suivante :
```python
python -m venv venv
```

#### **Activez l'environnement virtuel :**

Sur Windows :
```bash
venv\Scripts\activate
```

Sur macOS et Linux :
```bash
source venv/bin/activate
```

### 4. Installation des Dépendances
Installez les dépendances requises en utilisant la commande suivante pour lire le fichier requirements.txt :
```bash
pip install -r requirements.txt
```

### 5. Création de la base de données
Créer une base de données MySQL pour votre projet Django nommé "dbassociation", suivez ces étapes :

Installez MySQL :  
Si vous ne l'avez pas déjà fait, assurez-vous d'installer MySQL sur votre système. Vous pouvez télécharger la version appropriée pour votre système d'exploitation depuis le site officiel de MySQL (https://dev.mysql.com/downloads/).  

Créez une Base de Données :  
Une fois MySQL installé, vous pouvez créer une nouvelle base de données à l'aide de l'interface en ligne de commande.  
Ouvrez un terminal et connectez-vous à MySQL en utilisant un compte avec des privilèges d'administration. Vous serez invité à entrer le mot de passe du compte.
```ps
mysql -u root -p
```

Une fois connecté, vous pouvez créer une nouvelle base de données en utilisant la commande SQL suivante. Remplacez "dbassociation" par le nom de votre base de données souhaité.

```sql
CREATE DATABASE dbassociation;
```

Vous pouvez vérifier que la base de données a été créée en utilisant la commande suivante :

```sql
SHOW DATABASES;
```

__Configurer les Informations de Base de Données dans Django : __ 
Dans votre projet Django, ouvrez le fichier settings.py et localisez la section DATABASES. Vous devez configurer les informations de connexion à la base de données comme suit :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbassociation',
        'USER': 'votre_utilisateur_mysql',
        'PASSWORD': 'votre_mot_de_passe_mysql',
        'HOST': 'localhost',  # ou l'adresse de votre serveur MySQL
        'PORT': '',  # Laissez vide pour utiliser le port par défaut (3306)
    }
}
```
Assurez-vous de remplacer **_'votre_utilisateur_mysql'_**
et **_'votre_mot_de_passe_mysql'_**
par les informations de connexion appropriées pour votre serveur MySQL.

### 6.Migrations de la base de données
Assurez-vous d'avoir activé l'environnement virtuel (étape précédente). Ensuite, exécutez les migrations de la base de données en utilisant les commandes suivantes :
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7.Création d'un Superutilisateur
Pour accéder à l'interface d'administration Django, vous devez créer un superutilisateur en utilisant la commande suivante :
```bash
python manage.py createsuperuser
```
Suivez les instructions pour créer le superutilisateur en fournissant une adresse e-mail, un nom d'utilisateur, un nom, un prénom et un mot de passe.


### 8.Lancement du Serveur de Développement
Démarrez le serveur de développement Django en utilisant la commande suivante :

```bash
python manage.py runserver
```
Le serveur devrait démarrer, et vous pourrez accéder à l'application en ouvrant un navigateur web et en accédant à l'adresse http://localhost:8000/.

## 🚀 About Me
<a name="About Me"></a>
I'm a junior Python developer who try to code his life with a better framework than the one he used yesterday.

---
## 🔗 Links
<a name="Links"></a>
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/quentin-faure-b818221b9/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Q_Faure/)

---
## Tools

<center>
<a name="Tools"></a>
<p align="top left">
  <img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.svg" alt="Django" width="200" height="100">
</p>
<p align="top right">
  <img src="https://github.com/tus/official-images-docs/blob/master/mysql/logo.png?raw=true" alt="Django" width="200" height="90">
</p>

</center>