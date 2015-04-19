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

    $(".teams").click(function(){

        $('.highlight').removeClass('highlight');
        $(this).closest('li').addClass('highlight');

        $(".chart").hide();
        $(".buildjobUsageGraph").hide();
        $(".activeInuseServerGraph").hide();
        $(".totalBuildJobs").show();
    });


    $(".singleTeam").click(function(e){
        sessionStorage.setItem("teamName",e.target.innerHTML);

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

        $('.highlight').removeClass('highlight');
        $(this).addClass('highlight');

        var c = buildJobUsageObj.init();

        $(".totalBuildJobs").hide();
        $(".chart").hide();
        $(".activeInuseServerGraph").hide();
        $(".buildjobUsageGraph").show();
    });
   
});