if [ -f /etc/lsb-release ]; then
    echo "test"
    temp=$(grep DISTRIB_RELEASE /etc/lsb-release | cut -d= -f2)
    echo "$temp"
fi