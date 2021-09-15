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
        //  endDate:"-0d"
        // startDate:"-0d"

    }
    );

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

   