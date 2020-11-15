function myFunction() {
    // Declare variables
    var input, filter, marcas, a, h5, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    marcas = document.getElementById("marcas");
    a = marcas.getElementsByTagName("div");
    console.log(marcas);
    console.log(a);
    console.log(a.length);
    console.log(filter);

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < a.length; i++) {
        h6 = a[i].getElementsByTagName("h6")[0];
        if (h6) {
            txtValue = h6.textContent || h6.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                a[i].style.display = "block";
            } else {
                a[i].style.display = "none";
            }
        }
    }
}