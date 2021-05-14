FROM gitpod/workspace-full:latest
USER gitpod
RUN sudo apt-get install -y zsh && \
    curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | zsh && \
    chsh -s $(which zsh)
