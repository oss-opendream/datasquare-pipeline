./cluster_stop_all.sh
echo "Waiting for 3 seconds before starting cluster..."
sleep 3s

# 옵션이 없는 경우 처리
if [ $OPTIND -eq 1 ]; then
  ./cluster_start_all.sh
fi

# 옵션을 처리하는 함수
while getopts "a" opt; do
  case $opt in
    a)
      ./cluster_start_all.sh -a
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done
