{
    window.onload = () => {
        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(funcaoSucesso, funcaoErro);
        }
    }

    function funcaoSucesso(posicao: any) {
        var lat = posicao.coords.latitude;
        var lng = posicao.coords.longitude;
        console.log("Latitude: ", lat,"<br/>Longitude: ", lng);
    }

    function funcaoErro() {
        console.log("Deu erro...");
    }
}
{
    // https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition
    window.onload = inicia;
    function inicia() {
        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(funcaoSucesso, funcaoErro);
        }
    }

    function funcaoSucesso(posicao:GeolocationPosition) {
        var lat = posicao.coords.latitude;
        var lng = posicao.coords.longitude;
        console.log("Latitude: ", lat,"<br/>Longitude: ", lng);
    }

    function funcaoErro() {
        console.log("Deu erro...");
    }
}