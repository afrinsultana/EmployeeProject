$(function()
{
    // datepicker
    $("#id_dob").datepicker(
        {
        format:"yyyy-mm-dd",
        title:"Date of birth by Afrin",
        
        autoclose:true,
        orientation:"auto",
        todayHighlight:true,
        //  endDate:"-0d"  // date will not be shown after Today
        // startDate:"-0d" // Date will not be shown before today

    }
    );
    //show dialog
     $("#myModal").modal();

        setTimeout(() => {
           $('.alert').hide('slow'); 
        }, 5000);
   


    // show Image
    $('#id_photo').change(function(){
        readURL(this);
    });

    //Data Table
    $('#emptable').DataTable({
        'lengthMenu':[
            [1,3,5,10,20,50,-1],
            [1,3,5,10,20,50,'All']
        ]

    });

});

//
function readURL(input)
{
    if(input.files && input.files[0])
    {
        var reader=new FileReader();
        reader.onload=function(e)
        {
        
            $('.blah').attr('src',e.target.result);
        }
        reader.readAsDataURL(input.files[0]);

    }

}

   