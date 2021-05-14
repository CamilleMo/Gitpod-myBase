FROM gitpod/workspace-full
USER gitpod
RUN curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh && \
    chsh -s $(which zsh)
