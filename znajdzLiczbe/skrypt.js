var wylosowanaLiczba=Math.floor(Math.random()*100)+1;
function losuj(){
    var ilosc=document.getElementById('zakres').value;
    document.getElementById('wybranaWartosc').value=ilosc;
    wylosowanaLiczba=Math.floor(Math.random()*ilosc)+1;
}

function sprawdz(){
    let dane=document.getElementById("liczbaUzytkownika")
    if(dane.value == wylosowanaLiczba){
        alert("Wygrałeś");
    }else if(dane.value<wylosowanaLiczba){
        alert("Za mała liczba");
    }else{
        alert("Za duża liczba");
    }
}