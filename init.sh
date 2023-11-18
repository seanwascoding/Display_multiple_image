# source env36/bin/activate
# state=0
if [ -f /etc/lsb-release ];
then
    temp=$(grep DISTRIB_RELEASE /etc/lsb-release | cut -d= -f2)
    if [ "$temp" = "18.04" ];
    then
        state=0
    else
        state=1
    fi
else
    echo "fail"
fi

if [ "$state" = 0 ];
then
    pip install -r requirements-18.04.txt
elif [ "$state" = 1 ];
then
    pip install -r requirements-22.txt
fi


# if pip show opencv-python &>/dev/null && pip show opencv-contrib-python &>/dev/null
# then
#     echo "The package installed"
# else
#     echo "The package isn't exist"
#     pip install -r requirements.txt
# fi