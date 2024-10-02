#!/bin/bash

# 서버 배열
servers=( \
  "ds-db" \
  "ds-server" \
  "kafka1" \
  "kafka2" \
  "kafka3" \
  "kafka4" \
  "minio" \
  "elk" \
  )

# 현재 서버에서 git push 및 git pull 실행
echo "Running git push and pull on current server"
git push
git pull

# 현재 브랜치 및 리포지토리 이름 가져오기
current_branch=$(git rev-parse --abbrev-ref HEAD)
repo_name=$(basename `git rev-parse --show-toplevel`)

echo "Current branch: $current_branch"
echo "Repository name: $repo_name"

# 다른 서버로 ssh 접속하여 git pull 및 checkout 실행
for server in "${servers[@]}"; do
    # 현재 서버는 제외
    if [[ "$server" == "$(hostname)" ]]; then
        echo "Skipping current server: $server"
        continue
    fi

    echo "Connecting to $server..."

    ssh "$server" << EOF
        # 리포지토리 디렉토리로 이동
        cd ~/"$repo_name" || { echo "Repository $repo_name not found on $server"; exit 1; }

        # git pull 실행
        echo "Running git pull on $server in repository $repo_name"
        git pull --rebase

        # 브랜치 체크아웃
        echo "Checking out branch $current_branch on $server"
        git checkout "$current_branch"
EOF

done

echo "Script execution complete."
