
async function handlePageLoad(){
    const resp = await axios.get("/api/cupcakes");
    const cupcakes = resp.data['cupcakes'];
    fill_cupcakes(cupcakes);
    }


    // show_cupcakes();


function fill_cupcakes(cupcakes){

    for(let cupcake of cupcakes){
       const li =  $("<li></li>");
       li.text(cupcake.flavor);
        $('ul').append(li);
    }
}


$("#btn_add_cupcake").click(addCupcake);

async function addCupcake(){
    const flavor = $("#flavor").val();
    const size = $('#size').val();
    const rating = $('#rating').val();
    const image = $('#image').val();

    const resp = await axios.post("/api/cupcakes", {"flavor": flavor, "size": size, "rating": rating, "image": image}, {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    
    $("#flavor").val('');
    $('#size').val('');
    $('#rating').val('');
    $('#image').val('');

     const li =  $("<li></li>");
       li.Text(flavor);
        $('ul').append(li);
}


$(document).ready(handlePageLoad);