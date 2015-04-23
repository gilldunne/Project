/**
 * Created by Gillian on 07/04/2015.
 */


var pageSetup = function(){
    $(".chart").hide();
    $(".buildjobUsageGraph").hide();
    $(".activeInuseServerGraph").hide();
};

$(document).ready(function(){
    pageSetup();

    $(".dropDown").change(function(e){
        if(e.target.options[e.target.selectedIndex].text == "ALL"){
            sessionStorage.setItem("computerName","null");
            location.reload();
        }
        if(e.target.options[e.target.selectedIndex].text == "Ireland"){
            sessionStorage.setItem("computerName","test1.ie.ibm.com");
            location.reload();
        }
        else {
            location.reload();
            sessionStorage.setItem("computerName","test1.uk.ibm.com");
        }
    });

    $(".teams").click(function(){
        // highlight the navbar
        $('.highlight').removeClass('highlight');
        $(this).closest('li').addClass('highlight');

        $(".chart").hide();
        $(".buildjobUsageGraph").hide();
        $(".activeInuseServerGraph").hide();
        $(".totalBuildJobs").show();
    });


    $(".singleTeam").click(function(e){
        sessionStorage.setItem("teamName",e.target.innerHTML);
        // highlight the navbar
        $('.highlight').removeClass('highlight');
        $(this).closest('li').addClass('highlight');

        var a = componentBuildJobsObj.init();
        var b = activeInuseServersObj.init();

        $(".buildjobUsageGraph").hide();
        $(".totalBuildJobs").hide();
        $(".chart").show();
        $(".activeInuseServerGraph").show();

    });

    $(".singleComponent").click(function(e){

        sessionStorage.setItem("componentName",e.target.innerHTML);
        // highlight the navbar
        $('.highlight').removeClass('highlight');
        $(this).addClass('highlight');

        var c = buildJobUsageObj.init();

        $(".totalBuildJobs").hide();
        $(".chart").hide();
        $(".activeInuseServerGraph").hide();
        $(".buildjobUsageGraph").show();
    });
});
